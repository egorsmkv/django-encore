var Encore = require('@symfony/webpack-encore');

Encore
  // directory where compiled assets will be stored
  .setOutputPath('assets_build/build/')

  // public path used by the web server to access the output path
  .setPublicPath('/static/build')

  // only needed for CDN's or sub-directory deploy
  .setManifestKeyPrefix('static/build/')

  /*
   * ENTRY CONFIG
   *
   * Add 1 entry for each "page" of your app
   * (including one that's included on every page - e.g. "app")
   *
   * Each entry will result in one JavaScript file (e.g. app.js)
   * and one CSS file (e.g. app.css) if you JavaScript imports CSS.
   */

  .addEntry('app', './assets/js/app.js')
  .addEntry('demo1', './assets/js/demo1.js')

  .splitEntryChunks()

  // will require an extra script tag for runtime.js
  // but, you probably want this, unless you're building a single-page app
  .enableSingleRuntimeChunk()

  /*
   * FEATURE CONFIG
   *
   * Enable & configure other features below. For a full
   * list of features, see:
   * https://symfony.com/doc/current/frontend.html#adding-more-features
   */
  .cleanupOutputBeforeBuild()

  .enableBuildNotifications()
  .enableSourceMaps(!Encore.isProduction())

  // enables hashed filenames (e.g. app.abc123.css)
  .enableVersioning(Encore.isProduction())

  // enables Sass/SCSS support
  .enableSassLoader()

  // uncomment if you use TypeScript
  //.enableTypeScriptLoader()

  // uncomment if you're having problems with a jQuery plugin
  // .autoProvidejQuery()

  // uncomment if you use API Platform Admin (composer req api-admin)
  //.enableReactPreset()
;

module.exports = Encore.getWebpackConfig();
