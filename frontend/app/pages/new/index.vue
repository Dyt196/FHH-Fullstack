<script setup lang="ts">


const patient_name = ref<string>('')
const notes = ref<string>('')
const selectedCodes = ref<string[]>([])

async function submit (){
    if(!patient_name.value || !notes.value || selectedCodes.value.length === 0) {
        alert('Please fill all fields')
        return
    } else {
        await $fetch('http://localhost:8000/consultation', {
            method: 'POST',
            body: {
            patient_name: patient_name.value,
            notes: notes.value,
            diagnosis_codes: selectedCodes.value
            }
        })

        alert('Saved!')
        navigateTo('/')
    }
}

</script>

<template>
  <div class="p-6">
    <div class="flex items-center gap-4">
        <div class="flex items-center gap-2">
            <button @click="navigateTo('/')" class="text-gray-500 hover:text-gray-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
            </button>
        </div>
        <h1 class="text-2xl font-bold mb-4">New Consultation</h1>
    </div>

    <input v-model="patient_name" placeholder="Patient Name" class="border p-2 w-full mb-3" />

    <textarea v-model="notes" placeholder="Notes" class="border p-2 w-full mb-3"></textarea>

    <DiagnosisSearch v-model="selectedCodes"/>

    <button @click="submit" class="bg-green-500 text-white px-4 py-2 rounded mt-4">
      Save
    </button>
  </div>
</template>