var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    mode: "development",
    context: __dirname,

    entry: './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

    output: {
        path: path.resolve('./assets/bundles/'),
        filename: "[name]-[hash].js",
    },

    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
    ],

    module: {
        rules: [
            {   test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query:
                {
                    presets: ['@babel/preset-react']
                }
            }, // to transform JSX into JS
            {
                test: /\.scss$/,
            use: [
                "style-loader", // creates style nodes from JS strings
                "css-loader", // translates CSS into CommonJS
                "sass-loader" // compiles Sass to CSS, using Node Sass by default
            ]
            }
        ],
        


    },

    resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.js', '.jsx']
    },
}