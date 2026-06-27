<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">home</RouterLink>
        <RouterLink to="/api/v1/hw">test</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
>
