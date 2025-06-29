import { defineStore } from 'pinia';

export const useSnackbar = defineStore('snackbar', () => {
    const queue = ref([]);

    function add(item) {
        queue.value.push(item);
    }

    function addInfo(text) {
        add({
            text,
            color: 'info'
        });
    }

    function addSuccess(text) {
        add({
            text,
            color: 'success'
        });
    }

    function addWarning(text) {
        add({
            text,
            color: 'warning'
        });
    }

    function addError(text) {
        add({
            text,
            color: 'error'
        });
    }

    return {
        queue,
        add,
        addInfo,
        addSuccess,
        addWarning,
        addError
    };
});