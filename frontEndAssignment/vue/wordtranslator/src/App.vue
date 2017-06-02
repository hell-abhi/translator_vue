<template>
  <div id="app">
    <h1>Word Translator</h1>
    <h5>Powered By Vue.js</h5>
    <TranslateForm v-on:formSubmit="translateText"></TranslateForm>
    <TranslateOutput v-text="translatedText"></TranslateOutput>
  </div>
</template>

<script>
import TranslateForm from './components/TranslateForm'
import TranslateOutput from './components/TranslateOutput'

export default {
  name: 'app',
  components: {
    TranslateForm,
    TranslateOutput
  },
  data: function () {
    return {
      translatedText: ''
    }
  },
  methods: {
    translateText: function (text, language) {
      this.$http.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170530T080549Z.955b915d82374f3d.b2feb237679f043c6b8e6e68539416a9be087ad6&lang=' + language + '&text=' + text)
        .then((response) => {
          this.translatedText = response.body.text[0]
        })
    }
  }
}
</script>
