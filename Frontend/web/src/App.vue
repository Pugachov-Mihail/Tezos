<template>
  <div id="nav">
    <router-view />
  </div>
  <div>
    <img class="left" src="../src/assets/line_left.svg" alt="" />
    <img class="right" src="../src/assets/line_right.svg" />
  </div>
</template>

<style lang="sass">
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap')
//font-family: 'Roboto', sans-serif
body
  margin: 0
  padding: 0
  background: rgba(17, 21, 24, 1)

.left
  z-index: -1
  position: absolute
  top: 10%
  width: 100%
.right
  width: 100%
  z-index: -1
  position: absolute
  top: 40%
</style>
