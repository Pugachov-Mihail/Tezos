<template>
  <top-bar />
  <left-bar1 />
  <right-bar />
  <router-view :to="token"> </router-view>
</template>

<script>
import LeftBar1 from "@/components/LeftBar.vue";
import RightBar from "@/components/RightBar.vue";
import TopBar from "@/components/TopBar.vue";

export default {
  name: "Home",
  data() {
    return {
      token: true,
    };
  },
  components: {
    LeftBar1,
    RightBar,
    TopBar,
  },
};
</script>

<style lang="sass"></style>
