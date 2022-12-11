<template>
  <div id="app">
    <nav>
      <router-link to="/">Main</router-link> |
      <router-link :to="{ name: 'projects' }">Projects</router-link> |
      <router-link :to="{ name: 'peoples' }">People</router-link> |
      <router-link to="/">Community</router-link>
      <button class="btn btn-primary">Login</button>
      <button class="btn btn-primary">Sign in</button>
    </nav>
  <router-view>
  </router-view>
  <div>
  <!-- Footer -->
  <footer class="text-center text-lg-start bg-light text-muted" id="footer">
    <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
      © Copyright:<a class="text-reset fw-bold" href="/">rubat0@naver.com</a>
    </div>
  </footer>
  </div>
  </div>
</template>

<script>

export default {

}

</script>

<style>


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#footer {
    /* position: absolute;  */
    height: 100px;
    bottom: 0;
    width: 100%;
    position : relative;
    /* transform : translateY(-100%); */
}
</style>
