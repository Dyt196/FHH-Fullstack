<script setup lang="ts">
import type { Diagnosis } from '~/models/main'

const modelValue = defineModel<string[]>({default: () => []})

const search = ref('')
const results = ref<Diagnosis[]>([])
const allDiagnosis = ref<Diagnosis[]>([])
const config = useRuntimeConfig()

watch(search, async (val) => {
    const url = new URL(`${config.public.apiBase}/diagnosis`)
    if (val) {
        url.searchParams.append('search', val)
    }
    const res = await $fetch<Diagnosis[]>(url.toString())
    results.value = res
    
})

function addCode (code: string) {
  if (!modelValue.value.includes(code)) {
    modelValue.value.push(code)
  }
}

function removeCode (code: string) {
  modelValue.value = modelValue.value.filter(c => c !== code)
}

onMounted(async () => {
    const res = await $fetch<Diagnosis[]>(`${config.public.apiBase}/diagnosis`)
    results.value = res
    allDiagnosis.value = res
})
</script>

<template>
  <div>
    <input v-model="search" placeholder="Search diagnosis..." class="border p-2 w-full mb-2" />

    <div class="border max-h-40 overflow-auto">
      <div v-if="results.filter(r => !modelValue.includes(r.code)).length === 0" class="p-2 text-gray-500">
        No results found.
      </div>
      <div v-else
        v-for="item in results.filter(r => !modelValue.includes(r.code))"
        :key="item.code"
        class="p-2 hover:bg-gray-100 cursor-pointer"
        @click="addCode(item.code)"
      >
        {{ item.code }} - {{ item.description }}
      </div>
    </div>

    <div class="mt-2 flex gap-2 flex-wrap">
        <template v-for="code in modelValue.sort((a, b) => a.localeCompare(b))"
        :key="code">
            <div class="bg-blue-100 px-2 py-1 mr-2 rounded flex items-center">
                <div>
                {{ code }} - {{ allDiagnosis.find(r => r.code === code)?.description || 'N/A' }}
                </div>
                <button @click="removeCode(code)" class="text-red-500 ml-2">x</button>
            </div>
      </template>
    </div>
  </div>
</template>