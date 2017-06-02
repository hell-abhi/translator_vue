<template>
  <div id="translateForm">
    <form v-on:submit="formSubmit">
        <input type="text" v-model="textToTranslate" placeholder="Enter a word...">
        <select v-model="code">
            <option selected disabled>Choose Your Language</option>
            <option v-for="(languageName, languageCode) in languageList" v-bind:value="languageCode"> {{ languageName }} </option>
        </select>
        <input type="submit" value="Translate">
    </form>
  </div>
</template>

<script>
export default {
  name: 'translateForm',
  data () {
    return {
      textToTranslate: '',
      languageList: null,
      code: ''
    }
  },
  methods: {
    formSubmit (e) {
      this.$emit('formSubmit', this.textToTranslate, this.code)
      e.preventDefault()
    },
    getLanguageList () {
      this.$http.get('https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=' + 'trnsl.1.1.20170530T080549Z.955b915d82374f3d.b2feb237679f043c6b8e6e68539416a9be087ad6&ui=en')
      .then((response) => {
        // console.log(response.bodyText)
        var tempList = JSON.parse(response.bodyText)
        this.languageList = tempList.langs
        // console.log(this.languageList)
      })
    }
  },
  created () {
    this.getLanguageList()
  }
}
</script>
