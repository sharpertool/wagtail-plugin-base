const PLUGIN_NAME = process.env.PLUGIN_NAME || 'plugin-base';

module.exports = {
    entry: `./src/${PLUGIN_NAME}.js`,
    output: {
        filename: `${PLUGIN_NAME}.bundle.js`,
        path: __dirname + `/${PLUGIN_NAME}/static`
    }
};