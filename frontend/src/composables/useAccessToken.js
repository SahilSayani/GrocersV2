import { computed, ref } from "vue";

function useAccessToken() {
  const accessToken = ref("");

  return {
    accessToken,
  };
}
