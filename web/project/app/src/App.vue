<template>
    <body class="poster">
  <div id="app">
    <vue-particles
          color="#409EFF"
          :particleOpacity="0.7"
          :particlesNumber="60"
          shapeType="circle"
          :particleSize="6"
          linesColor="#409EFF"
          :linesWidth="1"
          :lineLinked="true"
          :lineOpacity="0.4"
          :linesDistance="150"
          :moveSpeed="3"
          :hoverEffect="true"
          hoverMode="grab"
          :clickEffect="true"
          clickMode="push"
          class="bg">
</vue-particles>

    <router-view/>
  </div>
    </body>
</template>

<style>
  .bg {
    width: 100%;
    height: calc(100% - 100px);
    position: absolute;

}
    .poster{
    height: 100%;
    width: 100%;
    top: 0px;
    left: 0px;
    margin: 0px;
    }
</style>
