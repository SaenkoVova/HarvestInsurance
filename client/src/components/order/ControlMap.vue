<template>
    <div>
        <div id="map" style="height: 500px; z-index: 1" />
        <v-snackbar
                v-model="snackbar"
                :timeout="2000"
        >
            Поле вже сформовано...
        </v-snackbar>
    </div>
</template>

<script>
    import L from 'leaflet';
    import {mapGetters, mapMutations} from "vuex";
    export default {
        data: () => ({
          map: null,
          markerCounter: 0,
          snackbar: false,
          icon: null
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
              attribution: 'Image tiles: &copy <a href="https://land.gov.ua/">ЦДЗК</a>'
          }).addTo(this.map);
          this.map.on('click', this.onMapClick)

        },
        methods: {
            ...mapMutations({
              setCoords: 'map/setCoords'
            }),
            onMapClick (e) {
                if (this.getCoords.length >= 4) { this.snackbar = true; return }
                L.marker(e.latlng, {icon: this.icon}).addTo(this.map);
                this.setCoords(e.latlng)
                console.log(e.latlng)
                if (this.getCoords.length === 4) {
                    this.setCoords(this.getCoords[0])
                    L.polygon(this.getCoords, { color: 'red' }).addTo(this.map)
                }
            }
        }
    }
</script>

<style>

</style>
