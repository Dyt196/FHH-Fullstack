<script setup lang="ts">
import type { Consultation, Diagnosis } from '~/models/main';

const props = defineProps<{
  data: Consultation[],
  diagnosisList: Diagnosis[]
}>()

function getDiagnosisDescription(code: string): string {
  const diag = props.diagnosisList.find(d => d.code === code)
  return diag ? diag.description : 'Unknown'
}
</script>

<template>
  <table class="w-full mt-4 border">
    <thead class="bg-gray-100">
      <tr>
        <th class="p-2">Patient</th>
        <th class="p-2">Notes</th>
        <th class="p-2">Diagnosis</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(consult,i) in data" :key="i" class="border-t">
        <td class="p-2">{{ consult.patientName }}</td>
        <td class="p-2">{{ consult.notes }}</td>
        <td class="p-2">
            <div class="flex flex-wrap">
                <template v-for="code in consult.diagnosisCodes" :key="code">
                    <div class="bg-blue-100 px-2 py-1 mr-2 mb-2 rounded">
                        {{ code }} - {{ getDiagnosisDescription(code) }}
                    </div> 
                </template>
            </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>