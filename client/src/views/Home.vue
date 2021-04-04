<template>
  <div>
    <paralax></paralax>
    <benefits-online-insurance></benefits-online-insurance>
    <insured-events></insured-events>
  </div>
</template>

<script>

import Paralax from '../components/home/ParalaxBaner'
import BenefitsOnlineInsurance from "@/components/home/BenefitsOnlineInsurance";
import InsuredEvents from "@/components/home/InsuredEvents";

export default {
  name: 'Home',
  components: {
    InsuredEvents,
    BenefitsOnlineInsurance,
    Paralax
  }
}
</script>
