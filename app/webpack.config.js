const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'development',
  entry: './shop/static/shop/app.js',
  output: {
    filename: 'bundled.js',
    path: path.resolve(__dirname, 'shop/static/shop'),
    publicPath: '/static/shop/',
  },
  devServer: {
    before: function(app, server, compiler) {
      server._watch('./**/*.html')
    },
    contentBase: 'http://localhost:8000',
    hot: true,
    proxy: {
      '!/static/shop/**': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
    port: 3000,
    host: '0.0.0.0',
  },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          'style-loader', // MiniCssExtractPlugin.loader
          'css-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/',
            },
          },
        ],
      },
    ],
  },
  /*plugins: [
    new MiniCssExtractPlugin({
      filename: 'bundled.css'
    })
  ],*/
};
