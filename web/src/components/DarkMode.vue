<!-- https://www.youtube.com/watch?v=cGN91TLXrC8&ab_channel=LearnVue -->
<script setup>
import { useDark, useToggle } from '@vueuse/core';

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>
<template>
  <!-- <p>isDark: {{ isDark }}</p> -->
  <button
    @click="toggleDark()"
    class="px-4 py-2 text-white right-5 w-12 h-12 bottom-5 fixed portrait:opacity-50 z-50"
  >
    <img
      class="right-5 w-12 h-12 bottom-5 fixed "
      src="https://i.ibb.co/f9hFgXQ/DALL-E-2023-07-02-21-32-31-scotch-whisky-in-a-Glencairn-glass-pixel-art-detailed-Copy-removebg-previ.png"
      alt="logo"
    />
    <!-- Toggle Dark Mode -->
  </button>
</template>
