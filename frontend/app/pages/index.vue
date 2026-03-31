<script setup lang="ts">
import type { Consultation, Diagnosis } from '~/models/main';

const consultations = ref<Consultation[]>([])
const diagnosisList = ref<Diagnosis[]>([])
const config = useRuntimeConfig()

async function getDiagnosisList() {
    const data = await $fetch<Diagnosis[]>(`${config.public.apiBase}/diagnosis`)
    diagnosisList.value = data || []
}

async function getConsultations() {
    const data = await $fetch<Consultation[]>(`${config.public.apiBase}/consultation`)
    consultations.value = data || []
}


onMounted(async () => {
    console.info("Config:", config.public.apiBase)
    await getConsultations()
    await getDiagnosisList()
})
</script>

<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Consultations</h1>
    Config: {{ config.public.apiBase }}

    <NuxtLink to="/new" class="bg-blue-500 text-white px-4 py-2 rounded">
      New Consultation
    </NuxtLink>

    <ConsultationTable :data="consultations" :diagnosis-list="diagnosisList" />
  </div>
</template>