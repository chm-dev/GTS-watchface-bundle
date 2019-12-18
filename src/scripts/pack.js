const { spawnSync } = require( 'child_process' );
const { renameSync, unlinkSync, statSync } = require( 'fs' );
const process = require( 'process' );
const path = require( 'path' );

const args = process.argv.splice( 2, process.argv.length );


if ( args.length < 1 ) throw 'Need folder path as input argument.';

const sourcePath = args[0];
const folderName = path.parse( args[0] ).name;
const jsonFile = path.join( args[0], folderName + '.json' );
const deflatedBin = path.join( sourcePath, `${folderName}_packed.bin` );
const inflatedBin = `${deflatedBin}.cmp`;

const outputPath = path.resolve( path.join( sourcePath, '..', '!out' ) );
const outputFilesPrefix = folderName.replace( '_unp', '' );

try {
  console.log( statSync( jsonFile ).isFile() );
}
catch ( e ) {
  throw e;
}
spawnSync(
  '..\\utils\\python-executable\\main.exe',
  ['--gts', '--file', jsonFile],
  {
    stdio: 'inherit'
  }
);

try {
  console.log( statSync( jsonFile ).isFile() );
}
catch ( e ) {
  throw e;
}

spawnSync( '..\\utils\\respacker.exe', [deflatedBin], {
  stdio: 'inherit'
} );
try {
  console.log( statSync( inflatedBin ).isFile() );
}
catch ( e ) {
  throw e;
}

renameSync( inflatedBin, path.join( outputPath, outputFilesPrefix + '.bin' ) );
renameSync(
  path.join(
    sourcePath,
    path.parse( inflatedBin ).base.replace( '.bin.cmp', '_animated.gif' )
  ),
  path.join( outputPath, outputFilesPrefix + '_animated.gif' ),
  {
    stdio: 'inherit'
  }
);
renameSync(
  path.join(
    sourcePath,
    path.parse( inflatedBin ).base.replace( '.bin.cmp', '_static.png' )
  ),
  path.join( outputPath, outputFilesPrefix + '_static.png' ),
  {
    stdio: 'inherit'
  }
);
