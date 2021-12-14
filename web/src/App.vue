<script setup lang="ts">
import VuePdfEmbed from "vue-pdf-embed";
import { useLocalStorage } from "@vueuse/core";

const isDark = useLocalStorage("isDark", false);

const redirect = (uri: string) => {
  window.location.href = uri;
};
</script>

<template>
  <div
    transition="all duration-150"
    :class="{ 'bg-black': isDark, 'bg-gray-100': !isDark }"
    pos="relative"
  >
    <div
      container="~"
      m="x-auto"
      w=" full md:1/2"
      transition="all duration-150"
      filter="~"
      :class="{ 'invert brightness-90': isDark }"
    >
      <vue-pdf-embed source="main.pdf" />
    </div>
    <div
      pos="fixed bottom-0 left-0 right-0"
      p="4"
      text="gray-700 xl"
      flex="~"
      justify="center"
    >
      <div
        flex="~"
        justify="evenly items-center"
        space="x-2"
        rounded="lg"
        bg="gray-200"
        p="2"
        opacity="90"
      >
        <button
          rounded="md"
          transition="all duration-150"
          hover:transform="~ scale-105"
          active:transform="~ scale-90"
          hover:bg="gray-300"
          p="1"
          @click="isDark = !isDark"
        >
          <carbon-sun v-if="!isDark" />
          <carbon-moon v-if="isDark" />
        </button>
        <button
          rounded="md"
          transition="all duration-150"
          hover:transform="~ scale-105"
          active:transform="~ scale-90"
          hover:bg="gray-300"
          p="1"
          @click="redirect('https://github.com/mkamadeus/final-report/')"
        >
          <carbon-logo-github />
        </button>
        <button
          rounded="md"
          transition="all duration-150"
          hover:transform="~ scale-105"
          active:transform="~ scale-90"
          hover:bg="gray-300"
          p="1"
          @click="redirect('main.pdf')"
        >
          <carbon-download />
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="postcss">
button {
  @apply flex items-center focus:outline-none;
}
</style>
