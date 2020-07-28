const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './shop/static/shop/app.js',
  output: {
    filename: 'bundled.js',
    path: path.resolve(__dirname, 'shop/static/shop'),
  },
  mode: 'development',
  watch: true,
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
