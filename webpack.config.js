const PLUGIN_NAME = process.env.PLUGIN_NAME || 'wagtail-katex';

module.exports = {
    entry: `./src/index.js`,
    output: {
        filename: `${PLUGIN_NAME}.bundle.js`,
        path: __dirname + `/${PLUGIN_NAME}/static`
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            '@babel/preset-env',
                            '@babel/preset-react'
                        ]
                    }
                }
            }
        ]
    },
    mode: 'development'
};