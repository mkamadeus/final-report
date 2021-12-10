<script setup lang="ts">
import VuePdfEmbed from "vue-pdf-embed";
import { ref } from "vue";
const isDark = ref(false);
</script>

<template>
  <div :class="{ 'bg-black': isDark, 'bg-gray-100': !isDark }" pos="relative">
    <div
      container="~"
      m="x-auto"
      w=" full md:1/2"
      filter="~"
      :class="{ 'invert brightness-90': isDark }"
    >
      <vue-pdf-embed source="main.pdf" />
    </div>
    <div
      pos="fixed bottom-0 left-0 right-0"
      p="4"
      text="white"
      flex="~"
      justify="center"
    >
      <div rounded="lg" bg="black" p="2" opacity="75">
        <button rounded="md" bg="green-400" p="2" @click="isDark = !isDark">
          <img src="/sun.svg" v-if="!isDark" />
          <img src="/moon.svg" v-if="isDark" />
        </button>
      </div>
    </div>
  </div>
</template>
