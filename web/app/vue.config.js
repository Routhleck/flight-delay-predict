const { defineConfig } = require('@vue/cli-service')
const {proxy} = require("vue/src/core/instance/state");
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: 'http://localhost:5000'
  }
})


