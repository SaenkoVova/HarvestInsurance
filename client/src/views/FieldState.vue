<template>
  <v-container>
    <div>
      <field-chart :height="300" id="1"></field-chart>
    </div>
  </v-container>
</template>

<script>
import FieldChart from "@/components/FieldState.vue/FieldChart";
export default {
  data: () => ({
  }),
  components: {
    FieldChart
  }
}
</script>
