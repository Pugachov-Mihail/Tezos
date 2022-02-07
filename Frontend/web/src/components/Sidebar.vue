<template>
  <div class="sidebar">
    <img class="logo" alt="logo" src="../assets/logo-full.png" />
    <div class="profil">
      <p>No profile</p>
    </div>
    <img class="men" src="../assets/premium-icon-vitruvian-man-3071121.png" alt="" />
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="sass">
.sidebar
  z-index: 100
  display: flex
  flex-direction: column
  background: linear-gradient(180deg, rgba(0, 0, 0, .60), rgba(37, 47, 29, .85), rgba(81, 105, 51, .60))
  width: 20%
  height: 100vh
.logo
  margin-left: 30%
  margin-top: 10%
  height: 10%
  width: 40%
.profil
  background: rgba(13, 13, 13, 0.65)
  margin-top: 7%
  margin-left: 25%
  width: 50%
  border: 1px solid rgba(255, 255, 255, 0.67)
  border-right: 0px
  border-top-left-radius: 15px
  border-bottom-left-radius: 15px
  p
    color: rgba(255, 255, 255, 1)
    text-align: center
    font-size: 25px
    font-family: 'Roboto', sans-serif
    padding: 10%
    margin: 0

.men
  margin-left: 35%
  margin-top: 8%
  height: 10%
  width: 30%
</style>
