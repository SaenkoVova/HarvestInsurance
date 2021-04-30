<script>
import { Line } from 'vue-chartjs'
export default {
  name: 'FieldState',
  extends: Line,
  props: {
    'id': {
      type: String,
      required: true
    }
  },
  data: () => ({
    gradient: null,
    gradient2: null
  }),
  mounted() {
    this.gradient = this.$refs.canvas.getContext(`2d`).createLinearGradient(0, 0, 0, 450)
    this.gradient2 = this.$refs.canvas.getContext(`2d`).createLinearGradient(0, 0, 0, 450)
    this.gradient.addColorStop(0, `rgba(255, 0,0, 0.5)`)
    this.gradient.addColorStop(0.5, `rgba(255, 0, 0, 0.25)`);
    this.gradient.addColorStop(1, `rgba(255, 0, 0, 0)`);

    this.gradient2.addColorStop(0, `rgba(0, 231, 255, 0.9)`)
    this.gradient2.addColorStop(0.5, `rgba(0, 231, 255, 0.25)`);
    this.gradient2.addColorStop(1, `rgba(0, 231, 255, 0)`);

    this.renderChart(
        {
          labels: ['2019-03', '2019-04', '2019-05', '2019-06', '2019-08', '2019-09', '2019-10', '2019-11', '2020-03', '2020-04', '2020-05', '2020-06', '2020-08', '2020-09', '2020-10', '2020-11'],
          datasets: [
            {
              backgroundColor: this.gradient2,
              borderColor: 'rgb(63,148,202)',
              lineTension: 0.1,
              pointRadius: 5,
              pointHoverRadius: 10,
              pointBackgroundColor: '#fff',
              data: [12, 13, 16, 35, 27, 20, 14, 3, 6, 8, 18, 17, 5, 6, 5, 6],
              lineWidth: 3,
              borderCapStyle: 'butt',
              borderWidth: 5,
              borderDash: [],
              strokeColor: "rgba(151,187,205,1)",
            },
            // {
            //   backgroundColor: this.gradient,
            //   borderColor: 'rgba(255, 0,0, 0.5)',
            //   lineTension: 0.1,
            //   pointRadius: 0,
            //   pointHoverRadius: 5,
            //   pointBackgroundColor: '#fff',
            //   data: [65, 9, 3, 65, 5, 76, 7, 8],
            //   lineWidth: 2,
            //   borderCapStyle: 'butt',
            //   borderWidth: 5,
            //   borderDash: [],
            //   strokeColor: "rgba(151,187,205,1)"
            // },
          ]
        },
        {
          responsive: true,
          maintainAspectRatio: false
        }
    );
  }
}
</script>
