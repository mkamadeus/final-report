import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import windicss from "vite-plugin-windicss";
import icons from "unplugin-icons/vite";
import autoimport from "unplugin-auto-import/vite";
import components from "unplugin-vue-components/vite";
import IconResolver from "unplugin-icons/resolver";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      "~/": `${path.resolve(__dirname, "src")}/`,
    },
  },
  plugins: [
    vue(),
    windicss(),
    autoimport({ dts: "src/auto-imports.d.ts" }),
    components({
      dts: "src/components.d.ts",
      extensions: ["vue"],
      resolvers: [
        IconResolver({
          componentPrefix: "",
        }),
      ],
    }),
    icons({ autoInstall: true, compiler: "vue3" }),
  ],
});
