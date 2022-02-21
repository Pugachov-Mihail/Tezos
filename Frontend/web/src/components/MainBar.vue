<template>
  <div class="form">
    <form action="/about">
      <h1>Введите свой токен</h1>
      <input :model="token" type="text" />
      <input class="btn" type="submit" value="Отправить" />
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      token: "",
    };
  },
  async created() {
    const response = await fetch("http://127.0.0.1:5000/", {
      type: "POST",
      //mode: "no-cors",
      contentType: "application/json; charset=utf-8",
      body: JSON.stringify(this.token),
    });
    this.users = await response.json();
  },
};
</script>

<style lang="sass" scoped>
.form
    margin-top: 15%
    margin-left: 37%
    input
      border: 1px solid white
      margin-left: -15%
      width: 65%
      height: 30px
      font-size: 27px
      background: black
      color: white
    .btn
        height: 30px
        margin-left: 3%
        width: 20%
</style>
