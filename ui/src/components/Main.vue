<template>
    <v-toolbar
        density="compact"
        image="../assets/toolbar-background.png"
        title="RDS Browser"
    >
        <v-dialog
            max-width="800"
        >
            <template
                v-slot:activator="{ props: activatorProps }"
            >
                <v-btn
                    v-bind="activatorProps"
                    prepend-icon="mdi-database-plus"
                    text="Add Database"
                    variant="tonal"
                />
            </template>
            <template
                v-slot:default="{ isActive }"
            >
                <v-form
                    v-model="addDatabaseFormIsValid"
                    @submit.prevent="submitAddDatabase(isActive)"
                >
                    <v-card
                        prepend-icon="mdi-database-plus"
                        title="Add Database"
                    >
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col
                                        cols="12"
                                        md="8"
                                    >
                                        <v-text-field
                                            v-model="addDatabaseUniqueId"
                                            v-maska="addDatabaseUniqueIdMaskaOptions"
                                            append-inner-icon="mdi-dice-multiple"
                                            label="Unique ID"
                                            placeholder="01234567-89ab-cdef-fedc-ba9876543210"
                                            prepend-inner-icon="mdi-identifier"
                                            :rules="addDatabaseUniqueIdRules"
                                            variant="solo-filled"
                                            @click:append-inner="getRandomAddDatabaseUniqueId"
                                        />
                                    </v-col>
                                    <v-col
                                        cols="12"
                                        md="4"
                                    >
                                        <v-switch
                                            v-model="addDatabaseIsSaveSpecific"
                                            color="secondary"
                                            label="Save-Specific"
                                            prepend-icon="mdi-content-save-check"
                                        />
                                    </v-col>
                                </v-row>
                            </v-container>
                            <v-alert
                                :icon="addDatabaseIsSaveSpecific ? 'mdi-content-save' : 'mdi-web'"
                                :text="addDatabaseIsSaveSpecific ? 'As a save-specific database, PlumbBuddy will automatically embed this database inside save files under the assumption you intend to populate it with data specific to a particular save (e.g. sims, households, etc.).' : 'As a global database, PlumbBuddy will store this database in a permanent location outside of save files, granting it better transaction handling and availability from Manage Worlds and the Main Menu screen.'"
                                type="info"
                                variant="tonal"
                                />
                            <p
                                class="mt-8"
                            >
                                Example script mod Python:
                            </p>
                            <highlightjs
                                :code="addDatabaseExamplePython"
                                language="py"
                            />
                            <p
                                class="mt-8"
                            >
                                Example bridged UI Javascript:
                            </p>
                            <highlightjs
                                :code="addDatabaseExampleJavaScript"
                                language="js"
                            />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn
                                prepend-icon="mdi-cancel"
                                text="Cancel"
                                @click="cancelAddDatabase(isActive)"
                            />
                            <v-btn
                                color="primary"
                                :disabled="!addDatabaseFormIsValid"
                                prepend-icon="mdi-plus"
                                text="Add Database"
                                type="submit"
                            />
                        </v-card-actions>
                    </v-card>
                </v-form>
            </template>
        </v-dialog>
        <v-btn
            class="ml-2"
            prepend-icon="mdi-book-open"
            text="Technical Documentation"
            variant="tonal"
            @click="openTechDocs"
        />
        <template
            v-if="persistedState.databases.length"
            v-slot:extension
        >
            <v-tabs
                v-model="persistedState.selectedTab"
            >
                <v-tab
                    v-for="database in persistedState.databases"
                    :value="`${database.uniqueId}-${database.isSaveSpecific ? 'S' : 'G'}`"
                >
                    <v-icon
                        class="mr-2"
                        :icon="`mdi-database${database.isSaveSpecific ? '-marker' : ''}`"
                    />
                    {{ database.uniqueId }}
                    <v-dialog
                        max-width="550"
                    >
                        <template
                            v-slot:activator="{ props: activatorProps }"
                        >
                            <v-icon-btn
                                v-bind="activatorProps"
                                class="ml-2"
                                icon="mdi-close"
                                size="small"
                                variant="tonal"
                            />
                        </template>
                        <template
                            v-slot:default="{ isActive }"
                        >
                            <v-card
                                prepend-icon="mdi-database-remove"
                                :subtitle="`Unique ID: ${database.uniqueId}${database.isSaveSpecific ? ' (Save-Specific)' : ' (Global)'}`"
                                title="Are you sure you want to close this database?"
                            >
                                <v-card-text
                                    class="d-flex flex-column ga-2"
                                >
                                    <v-alert
                                        text="Closing this database's tab will not delete its data."
                                        type="info"
                                        />
                                    <v-alert
                                        text="If you want to browse this database again, you will have to add it again using ADD DATABASE above."
                                        type="warning"
                                        />
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer />
                                    <v-btn
                                        prepend-icon="mdi-cancel"
                                        text="Cancel"
                                        @click="isActive.value = false"
                                    />
                                    <v-btn
                                        color="warning"
                                        prepend-icon="mdi-close"
                                        text="Close Database"
                                        @click="closeDatabase(database, isActive)"
                                    />
                                </v-card-actions>
                            </v-card>
                        </template>
                    </v-dialog>
                </v-tab>
            </v-tabs>
        </template>
    </v-toolbar>
    <v-tabs-window
        v-model="persistedState.selectedTab"
        class="database-tabs"
    >
        <v-tabs-window-item
            v-for="database in persistedState.databases"
            :value="`${database.uniqueId}-${database.isSaveSpecific ? 'S' : 'G'}`"
        >
            <DatabaseTab
                :unique-id="database.uniqueId"
                :is-save-specific="database.isSaveSpecific"
            />
        </v-tabs-window-item>
    </v-tabs-window>
</template>

<script setup>
    import { vMaska } from 'maska/vue';
    import { usePersistedState } from '@/stores/global-state';

    const persistedState = usePersistedState();
    
    const addDatabaseFormIsValid = shallowRef(false);
    const addDatabaseUniqueId = ref('');
    const addDatabaseUniqueIdMaskaOptions = reactive({
        mask: 'HHHHHHHH-HHHH-HHHH-HHHH-HHHHHHHHHHHH',
        tokens: {
            H: {
                pattern: /[\da-f]/i
            }
        },
    });
    const addDatabaseIsSaveSpecific = ref(false);

    const addDatabaseExamplePython = computed(() => `try:
    from plumbbuddy_proxy.api import gateway
    from uuid import UUID
    unique_id = UUID('${addDatabaseUniqueId.value}')
    database = gateway.get_relational_data_storage(unique_id, ${addDatabaseIsSaveSpecific.value ? 'True' : 'False'})
except ModuleNotFoundError:
    # either PlumbBuddy is unavailable or RMI has been disabled by the player
    # handling this is the mod's responsibility, unfortunately
    pass`);
    const addDatabaseExampleJavaScript = computed(() => `const uniqueId = '${addDatabaseUniqueId.value}';
const database = gateway.getRelationalDataStorage(uniqueId, ${addDatabaseIsSaveSpecific.value ? 'true' : 'false'});`);

    function getRandomAddDatabaseUniqueId() {
        addDatabaseUniqueId.value = gateway.uuid4();
    }

    const addDatabaseUniqueIdRules = [
        value => {
            if (value.length === 36) {
                return true;
            }
            return 'Unique ID is required.';
        },
    ];

    function cancelAddDatabase(isActive) {
        isActive.value = false;
        addDatabaseUniqueId.value = '';
        addDatabaseIsSaveSpecific.value = false;
    }

    function submitAddDatabase(isActive) {
        isActive.value = false;
        if (persistedState.value.databases.findIndex(database => database.uniqueId === addDatabaseUniqueId.value && database.isSaveSpecific === addDatabaseIsSaveSpecific.value) < 0) {
            persistedState.value.databases.push({
                uniqueId: addDatabaseUniqueId.value,
                isSaveSpecific: addDatabaseIsSaveSpecific.value,
            });
        }
        persistedState.value.selectedTab = `${addDatabaseUniqueId.value}-${addDatabaseIsSaveSpecific.value ? 'S' : 'G'}`;
        addDatabaseUniqueId.value = '';
        addDatabaseIsSaveSpecific.value = false;
    }

    function openTechDocs() {
        gateway.openUrl('https://github.com/Llama-Logic/PlumbBuddy/wiki/Relational-Data-Storage');
    }

    function closeDatabase(database, isActive) {
        const { uniqueId, isSaveSpecific } = database;
        persistedState.value.databases.splice(persistedState.value.databases.indexOf(database), 1);
        if (persistedState.value.tabStates) {
            const tabStateId = `${uniqueId}-${isSaveSpecific ? 'S' : 'G'}`;
            if (persistedState.value.tabStates[tabStateId]) {
                delete persistedState.value.tabStates[tabStateId];
            }
        }
        isActive.value = false;
    }
</script>