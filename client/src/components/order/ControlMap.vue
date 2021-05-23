<template>
    <v-row>
      <v-col :cols="9">
        <div id="map" style="height: 500px; z-index: 1" />
      </v-col>
      <v-col :cols="3">
        <v-btn block large color="primary" @click="clearCoords">Очистити кординати</v-btn>
      </v-col>
      <v-snackbar
              v-model="snackbar"
              :timeout="2000"
      >
          Поле вже сформовано...
      </v-snackbar>
    </v-row>
</template>

<script>
    import L from 'leaflet';
    import {mapGetters, mapMutations} from "vuex";
    export default {
        data: () => ({
          map: null,
          markerCounter: 0,
          snackbar: false,
          icon: null,
          layerGroup: null
        }),
        computed: {
          ...mapGetters({
            getCoords: 'map/getCoords'
          })
        },
        mounted () {
          this.map = L.map('map', {
              center: [48.505, 30.967],
              zoom: 6
          })
          let leafIcon = L.Icon.extend({
            options: {
              iconSize:     [38, 95],
              shadowSize:   [50, 64],
              iconAnchor:   [22, 94],
              shadowAnchor: [4, 62],
              popupAnchor:  [-3, -76]
            }
          });
          this.icon = new leafIcon({
            iconUrl: 'http://leafletjs.com/examples/custom-icons/leaf-green.png',
            shadowUrl: 'http://leafletjs.com/examples/custom-icons/leaf-shadow.png'
          })
          L.tileLayer.wms('http://ows.mundialis.de/services/service?', {
              layers: 'TOPO-OSM-WMS',
              format: 'image/png',
              transparent: true,
          }).addTo(this.map);
          this.layerGroup = L.layerGroup().addTo(this.map);
          this.map.on('click', this.onMapClick);
          this.initMapFromStore();
        },
        methods: {
            ...mapMutations({
              setCoords: 'map/setCoords',
              unsetCoords: 'map/unsetCoords'
            }),
            initMapFromStore() {
              if(!this.getCoords.length) {
                return;
              }
              this.getCoords.map(i => L.marker(i, {icon: this.icon}).addTo(this.layerGroup))
              L.polygon(this.getCoords, { color: 'red' }).addTo(this.layerGroup)
            },
            clearCoords() {
              this.unsetCoords();
              this.layerGroup.clearLayers();
            },
            onMapClick (e) {
                if (this.getCoords.length >= 4) { this.snackbar = true; return }
                L.marker(e.latlng, {icon: this.icon}).addTo(this.layerGroup);
                this.setCoords(e.latlng)
                if (this.getCoords.length === 4) {
                    this.setCoords(this.getCoords[0])
                    L.polygon(this.getCoords, { color: 'red' }).addTo(this.layerGroup)
                }
            }
        }
    }
</script>

<style>

</style>
