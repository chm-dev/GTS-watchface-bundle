const { app, BrowserWindow } = require( 'electron' );
const path = require( 'path' );
const { format } = require( 'url' );
const process = require( 'process' );
const { resolve } = require( 'path' );
const entrypoint = format( {
  pathname: resolve( __dirname, '..', 'index.html' ),
  protocol: 'file',
  slashes: true
} );
let mainWindow;
const ico = resolve( __dirname, '..', 'assets/icon/win-icon.ico' );

function createWindow( w, h ) {
  // Create the browser window.
  mainWindow = new BrowserWindow( {
    width: w,
    height: h,
    autoHideMenuBar: true,
    center: true,
    resizable: true,
    movable: true,
    minimizable: true,
    maximizable: true,
    closable: true,
    skipTaskbar: false,
    icon: ico,
    webPreferences: {
      webSecurity: true
    },
    frame: true,
    transparent: false
  } );

  mainWindow.loadURL( entrypoint );
  const contents = mainWindow.webContents;

  mainWindow.webContents.on( 'did-finish-load', function() {
    contents.insertCSS(
      `
      .navbar {-webkit-app-region: drag;}
      .navbar-history, .navbar-search, .navbar-nav__item {-webkit-app-region: no-drag;}
      `
    );
  } );
}
app.on( 'ready', () => {
  createWindow( 1024, 960 );
} );

// Quit when all windows are closed.
app.on( 'window-all-closed', () => {
  // On macOS it is common for applications and their menu bar to stay active
  // until the user quits explicitly with Cmd + Q
  if ( process.platform !== 'darwin' ) {
    app.quit();
  }
} );

app.on( 'activate', () => {
  // On macOS it's common to re-create a window in the app when the dock icon is
  // clicked and there are no other windows open.
  if ( mainWindow === null ) {
    createWindow();
  }
} );
