<template>
  <v-container>
    <h1 class="display-1">Cadastral number</h1>
    <div>
      <field-chart :height="300" id="1" :ndvi="ndvi" :dates="dates" v-if="loaded"></field-chart>
    </div>
  </v-container>
</template>

<script>
import FieldChart from "@/components/FieldState.vue/FieldChart";
import http from "../util/http";
export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data: () => ({
    ndvi: [],
    dates: [],
    loaded: false
  }),
  methods: {
    loadOrderDetails() {
      http.get('loadOrderDetails/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        params: {
          police_id: this.id
        }
      })
          .then(res => {
            this.ndvi = res.data.ndvi.filter(i => i !== 0)
            this.dates = res.data.dates
            this.loaded = true;
          })
    },
  },
  mounted() {
    this.loadOrderDetails()
  },
  components: {
    FieldChart
  }
}
</script>
