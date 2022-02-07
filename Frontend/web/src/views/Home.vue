<template>
  <div class="home">
    <sidebar />
  </div>
</template>

<script>
// @ is an alias to /src
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "Home",
  components: {
    Sidebar,
  },
};
</script>
