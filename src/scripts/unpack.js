const { spawnSync } = require( 'child_process' );
const { renameSync, unlinkSync } = require( 'fs' );
const process = require( 'process' );

const args = process.argv.splice( 2, process.argv.length );
console.log( __dirname );
if ( args.length < 1 ) throw 'Need bin file as input argument.';

spawnSync( '..\\utils\\resunpacker.exe', args, {
  stdio: 'inherit'
} );
const newFile = `${args[0]}.unp`.replace( '.bin.unp', '_unp.bin' );
console.log( newFile );
renameSync( `${args[0]}.unp`, newFile, {
  stdio: 'inherit'
} );
spawnSync(
  '..\\utils\\python-executable\\main.exe',
  ['--gts', '--file', `${newFile}`],
  {
    stdio: 'inherit'
  }
);
unlinkSync( newFile );