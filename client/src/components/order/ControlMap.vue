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
    export default {
        data: () => ({
            map: null,
            markerCounter: 0,
            latlngs: [],
            snackbar: false
        }),
        mounted () {
            this.map = L.map('map', {
                center: [48.505, 30.967],
                zoom: 6
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
            onMapClick (e) {
                if (this.latlngs.length >= 4) { this.snackbar = true; return }
                L.marker(e.latlng).addTo(this.map);
                this.latlngs.push(e.latlng);
                if (this.latlngs.length === 4) {
                    this.latlngs.push(this.latlngs[0]);
                    L.polygon(this.latlngs, { color: 'red' }).addTo(this.map)
                }
            }
        }
    }
</script>

<style>

</style>
