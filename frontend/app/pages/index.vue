<script setup lang="ts">
import type { Consultation, Diagnosis } from '~/models/main';

const consultations = ref<Consultation[]>([])
const diagnosisList = ref<Diagnosis[]>([])

async function getDiagnosisList() {
    const { data } = await useFetch<Diagnosis[]>('http://localhost:8000/diagnosis')
    diagnosisList.value = data.value || []
}

async function getConsultations() {
    const { data } = await useFetch<Consultation[]>('http://localhost:8000/consultation')
    consultations.value = data.value || []
}


onMounted(async () => {
    await getConsultations()
    await getDiagnosisList()
})
</script>

<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Consultations</h1>

    <NuxtLink to="/new" class="bg-blue-500 text-white px-4 py-2 rounded">
      New Consultation
    </NuxtLink>

    <ConsultationTable :data="consultations" :diagnosis-list="diagnosisList" />
  </div>
</template>