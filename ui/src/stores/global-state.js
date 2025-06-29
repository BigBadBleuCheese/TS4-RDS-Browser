import { createGlobalState, useStorage } from '@vueuse/core';

export const usePersistedState = createGlobalState(() => useStorage('ts4-rds-browser', {
    databases: [],
    selectedTab: null,
    tabStates: {},
    toolbarAnimation: 0,
}, localStorage));
