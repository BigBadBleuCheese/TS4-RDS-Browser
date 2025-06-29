<template>
    <div
        class="schema-objects pa-4 overflow-y-auto"
    >
        <v-expansion-panels
            v-model="tabState.openSchemaPanels"
            multiple
        >
            <v-expansion-panel
                value="tables"
            >
                <v-expansion-panel-title>
                    <v-icon>
                        mdi-table
                    </v-icon>
                    <span
                        class="ml-8"
                    >
                        Tables
                    </span>
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-list
                        class="pa-0 ma-n2 mx-n4"
                    >
                        <v-list-group
                            v-for="table in tables"
                        >
                            <template
                                v-slot:activator="{ props }"
                            >
                                <v-list-item
                                    v-bind="props"
                                    prepend-icon="mdi-table"
                                    :title="table.name"
                                >
                                    <v-list-item-action>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate SELECT statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="info"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateTableSelect(table)"
                                                >
                                                    <v-icon>
                                                        mdi-table-search
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate INSERT statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="secondary"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateTableInsert(table)"
                                                >
                                                    <v-icon>
                                                        mdi-table-row-plus-after
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate CREATE statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="primary"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="replaceSelectedCode(table.sql)"
                                                >
                                                    <v-icon>
                                                        mdi-table-plus
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate DROP statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="warning"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateTableDrop(table)"
                                                >
                                                    <v-icon>
                                                        mdi-table-remove
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                    </v-list-item-action>
                                </v-list-item>
                            </template>
                            <v-list-item
                                v-for="column in table.columns"
                                :prepend-icon="column.isPrimaryKey ? 'mdi-key' : 'mdi-table-column'"
                                :subtitle="`${column.type}${column.isNotNull ? ' NOT NULL' : ''}`"
                                :title="column.name"
                            />
                        </v-list-group>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel
                value="indicies"
            >
                <v-expansion-panel-title>
                    <v-icon>
                        mdi-sort
                    </v-icon>
                    <span
                        class="ml-8"
                    >
                        Indicies
                    </span>
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-list
                        class="pa-0 ma-n2 mx-n4"
                    >
                        <v-list-item
                            v-for="index in indicies"
                            prepend-icon="mdi-sort"
                            :subtitle="index.table"
                            :title="index.name"
                        >
                            <v-list-item-action>
                                <v-tooltip
                                    location="bottom"
                                    text="Generate DROP and CREATE statement"
                                >
                                    <template
                                        v-slot:activator="{ props }"
                                    >
                                        <v-btn
                                            v-bind="props"
                                            color="warning"
                                            size="x-small"
                                            variant="tonal"
                                            @click.stop="generateIndexDropAndCreate(index)"
                                        >
                                            <v-icon>
                                                mdi-sort-bool-descending-variant
                                            </v-icon>
                                        </v-btn>
                                    </template>
                                </v-tooltip>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel
                value="views"
            >
                <v-expansion-panel-title>
                    <v-icon>
                        mdi-table-eye
                    </v-icon>
                    <span
                        class="ml-8"
                    >
                        Views
                    </span>
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-list
                        class="pa-0 ma-n2 mx-n4"
                    >
                        <v-list-group
                            v-for="view in views"
                        >
                            <template
                                v-slot:activator="{ props }"
                            >
                                <v-list-item
                                    v-bind="props"
                                    prepend-icon="mdi-table-eye"
                                    :title="view.name"
                                >
                                    <v-list-item-action>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate SELECT statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="primary"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateTableSelect(view)"
                                                >
                                                    <v-icon>
                                                        mdi-table-search
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate INSERT statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="secondary"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateTableInsert(view)"
                                                >
                                                    <v-icon>
                                                        mdi-table-row-plus-after
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate CREATE statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="primary"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="replaceSelectedCode(view.sql)"
                                                >
                                                    <v-icon>
                                                        mdi-table-plus
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                        <v-tooltip
                                            location="bottom"
                                            text="Generate DROP statement"
                                        >
                                            <template
                                                v-slot:activator="{ props }"
                                            >
                                                <v-btn
                                                    v-bind="props"
                                                    color="warning"
                                                    size="x-small"
                                                    variant="tonal"
                                                    @click.stop="generateViewDrop(view)"
                                                >
                                                    <v-icon>
                                                        mdi-table-remove
                                                    </v-icon>
                                                </v-btn>
                                            </template>
                                        </v-tooltip>
                                    </v-list-item-action>
                                </v-list-item>
                            </template>
                            <v-list-item
                                v-for="column in view.columns"
                                prepend-icon="mdi-table-column"
                                :subtitle="column.type"
                                :title="column.name"
                            />
                        </v-list-group>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel
                value="triggers"
            >
                <v-expansion-panel-title>
                    <v-icon>
                        mdi-script
                    </v-icon>
                    <span
                        class="ml-8"
                    >
                        Triggers
                    </span>
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <v-list
                        class="pa-0 ma-n2 mx-n4"
                    >
                        <v-list-item
                            v-for="trigger in triggers"
                            prepend-icon="mdi-script"
                            :subtitle="trigger.table"
                            :title="trigger.name"
                        >
                            <v-list-item-action>
                                <v-tooltip
                                    location="bottom"
                                    text="Generate DROP and CREATE statement"
                                >
                                    <template
                                        v-slot:activator="{ props }"
                                    >
                                        <v-btn
                                            v-bind="props"
                                            color="warning"
                                            size="x-small"
                                            variant="tonal"
                                            @click.stop="generateTriggerDropAndCreate(trigger)"
                                        >
                                            <v-icon>
                                                mdi-script-text
                                            </v-icon>
                                        </v-btn>
                                    </template>
                                </v-tooltip>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
    <div
        class="editor"
    >
        <v-toolbar
            title="Query Editor"
        >
            <v-tooltip
                location="bottom"
                text="Refresh Schema Objects"
            >
                <template
                    v-slot:activator="{ props }"
                >
                    <v-btn
                        v-bind="props"
                        class="ma-1"
                        icon="mdi-database-refresh"
                        size="small"
                        variant="flat"
                        @click="refreshSchema"
                    />
                </template>
            </v-tooltip>
            <v-divider
                class="mx-1"
                vertical
            />
            <v-tooltip
                location="bottom"
                text="Execute All SQL"
            >
                <template
                    v-slot:activator="{ props }"
                >
                    <v-btn
                        v-bind="props"
                        class="ma-1"
                        color="success"
                        icon="mdi-run"
                        size="small"
                        variant="flat"
                        @click="handleSendAllAndRun"
                    />
                </template>
            </v-tooltip>
            <v-tooltip
                location="bottom"
                text="Execute Selected SQL"
            >
                <template
                    v-slot:activator="{ props }"
                >
                    <v-btn
                        v-bind="props"
                        class="ma-1"
                        color="success"
                        :disabled="!selectedCode.length"
                        icon="mdi-run-fast"
                        size="small"
                        :variant="selectedCode.length ? 'flat' : 'tonal'"
                        @click="handleSendSelectionAndRun"
                    />
                </template>
            </v-tooltip>
            <v-divider
                class="mx-1"
                vertical
            />
            <v-tooltip
                location="bottom"
                text="Clear Results"
            >
                <template
                    v-slot:activator="{ props }"
                >
                    <v-btn
                        v-bind="props"
                        class="ma-1"
                        :disabled="!results.length"
                        icon="mdi-delete-empty"
                        size="small"
                        :variant="results.length ? 'flat' : 'tonal'"
                        @click="results = []"
                    />
                </template>
            </v-tooltip>
            <v-divider
                class="mx-1"
                vertical
            />
            <v-dialog>
                <template
                    v-slot:activator="{ props: activatorProps }"
                >
                    <v-btn
                        v-bind="activatorProps"
                        class="ma-1"
                        color="primary"
                        :icon="''"
                        size="small"
                        variant="flat"
                    >
                        <svg-icon type="mdi" :path="mdiLanguagePython"></svg-icon>
                        <v-tooltip
                            activator="parent"
                            location="bottom"
                            text="Show Example Script Mod Python for All SQL"
                        />
                    </v-btn>
                </template>
                <template
                    v-slot:default="{ isActive }"
                >
                    <v-card
                        title="Example Script Mod Python for All SQL"
                    >
                        <v-card-text>
                            <highlightjs
                                :code="examplePythonAllCode"
                                language="py"
                            />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn
                                prepend-icon="mdi-close"
                                text="Close"
                                @click="isActive.value = false"
                            />
                        </v-card-actions>
                    </v-card>
                </template>
            </v-dialog>
            <v-dialog>
                <template
                    v-slot:activator="{ props: activatorProps }"
                >
                    <v-btn
                        v-bind="activatorProps"
                        class="ma-1"
                        color="secondary"
                        :disabled="!selectedCode.length"
                        :icon="''"
                        size="small"
                        :variant="selectedCode.length ? 'flat' : 'tonal'"
                    >
                        <svg-icon type="mdi" :path="mdiLanguagePython"></svg-icon>
                        <v-tooltip
                            activator="parent"
                            location="bottom"
                            text="Show Example Script Mod Python for Selected SQL"
                        />
                    </v-btn>
                </template>
                <template
                    v-slot:default="{ isActive }"
                >
                    <v-card
                        title="Example Script Mod Python for Selected SQL"
                    >
                        <v-card-text>
                            <highlightjs
                                :code="examplePythonSelectedCode"
                                language="py"
                            />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn
                                prepend-icon="mdi-close"
                                text="Close"
                                @click="isActive.value = false"
                            />
                        </v-card-actions>
                    </v-card>
                </template>
            </v-dialog>
            <v-dialog>
                <template
                    v-slot:activator="{ props: activatorProps }"
                >
                    <v-btn
                        v-bind="activatorProps"
                        class="ma-1"
                        color="primary"
                        :icon="''"
                        size="small"
                        variant="flat"
                    >
                        <svg-icon type="mdi" :path="mdiLanguageJavascript"></svg-icon>
                        <v-tooltip
                            activator="parent"
                            location="bottom"
                            text="Show Example Bridged UI JavaScript for All SQL"
                        />
                    </v-btn>
                </template>
                <template
                    v-slot:default="{ isActive }"
                >
                    <v-card
                        title="Example Bridged UI JavaScript for All SQL"
                    >
                        <v-card-text>
                            <highlightjs
                                :code="exampleJavaScriptAllCode"
                                language="py"
                            />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn
                                prepend-icon="mdi-close"
                                text="Close"
                                @click="isActive.value = false"
                            />
                        </v-card-actions>
                    </v-card>
                </template>
            </v-dialog>
            <v-dialog>
                <template
                    v-slot:activator="{ props: activatorProps }"
                >
                    <v-btn
                        v-bind="activatorProps"
                        class="ma-1"
                        color="secondary"
                        :disabled="!selectedCode.length"
                        :icon="''"
                        size="small"
                        :variant="selectedCode.length ? 'flat' : 'tonal'"
                    >
                        <svg-icon type="mdi" :path="mdiLanguageJavascript"></svg-icon>
                        <v-tooltip
                            activator="parent"
                            location="bottom"
                            text="Show Example Bridged UI JavaScript for Selected SQL"
                        />
                    </v-btn>
                </template>
                <template
                    v-slot:default="{ isActive }"
                >
                    <v-card
                        title="Example Bridged UI JavaScript for Selected SQL"
                    >
                        <v-card-text>
                            <highlightjs
                                :code="exampleJavaScriptSelectedCode"
                                language="py"
                            />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn
                                prepend-icon="mdi-close"
                                text="Close"
                                @click="isActive.value = false"
                            />
                        </v-card-actions>
                    </v-card>
                </template>
            </v-dialog>
        </v-toolbar>
        <vue-monaco-editor
            v-model:value="tabState.code"
            language="sql"
            :options="MONACO_EDITOR_OPTIONS"
            theme="vs-dark"
            @mount="handleMount"
        />
    </div>
    <v-sheet
        class="results pa-2 overflow-y-auto"
    >
        <v-expansion-panels
            multiple
        >
            <v-expansion-panel
                v-for="result in results"
            >
                <v-expansion-panel-title
                >
                    <v-icon>
                        mdi-database-search
                    </v-icon>
                    <span
                        class="ml-1"
                    >
                        Query:
                    </span>
                    <pre
                        class="ml-1"
                    >{{ result.queryId }}</pre>
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                    <div
                        class="d-flex flex-column ga-2 pa-0 mb-n2 mx-n4"
                    >
                        <v-alert
                            v-if="result.errorMessage"
                            border="start"
                            color="error"
                            density="compact"
                            icon="mdi-database-alert"
                            :title="result.errorMessage"
                            variant="tonal"
                        >
                            <div
                                class="d-flex flex-column ga-2"
                            >
                                <p>
                                    The database got mad. It reported error code {{ result.errorCode }} and extended error code {{ result.extendedErrorCode }}.
                                </p>
                                <v-btn
                                    prepend-icon="mdi-open-in-new"
                                    text="Learn More from the SQLite Documentation"
                                    @click.stop="openSqliteErrorDocumentation"
                                />
                            </div>
                        </v-alert>
                        <v-alert
                            v-if="result.tag"
                            border="start"
                            color="info"
                            density="compact"
                            icon="mdi-tag"
                            text="This tag was supplied by whatever mod or component originally submitted the query."
                            :title="result.tag"
                            variant="tonal"
                        />
                        <v-alert
                            border="start"
                            color="info"
                            density="compact"
                            icon="mdi-timer"
                            text="This is the amount of time the database spent processing the query. If this query were submitted by a script mod, simulation load and result size might have contributed added delay to the player experience."
                            :title="`${result.executionDuration.format('HH:mm:ss')} + ${result.executionDuration.format('SSS')} ms`"
                            variant="tonal"
                        />
                        <v-expansion-panels
                            multiple
                        >
                            <v-expansion-panel
                                v-for="(recordSet, index) in result.recordSets"
                            >
                                <v-expansion-panel-title>
                                    <v-icon>
                                        mdi-table
                                    </v-icon>
                                    <span
                                        class="ml-2"
                                    >
                                        Record Set {{ index }}
                                    </span>
                                </v-expansion-panel-title>
                                <v-expansion-panel-text>
                                    <v-data-table
                                        color="primary"
                                        :items="recordSet.items"
                                    />
                                </v-expansion-panel-text>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </div>
                </v-expansion-panel-text>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-sheet>
</template>

<script setup>
    import dayjs from 'dayjs';
    import relativeTime from 'dayjs/plugin/relativeTime';
    import duration from 'dayjs/plugin/duration';
    import SvgIcon from '@jamescoyle/vue-icon';
    import { mdiLanguageJavascript, mdiLanguagePython } from '@mdi/js';
    import { usePersistedState } from '@/stores/global-state';

    dayjs.extend(relativeTime);
    dayjs.extend(duration);

    const { uniqueId, isSaveSpecific } = defineProps({
        uniqueId: String,
        isSaveSpecific: Boolean,
    });

    const persistedState = usePersistedState();
    if (!persistedState.value.tabStates) {
        persistedState.value.tabStates = {};
    }
    const tabStateId = `${uniqueId}-${isSaveSpecific ? 'S' : 'G'}`;
    if (!persistedState.value.tabStates[tabStateId]) {
        persistedState.value.tabStates[tabStateId] = {
            openSchemaPanels: ['tables'],
        };
    }
    const tabState = persistedState.value.tabStates[tabStateId];

    const tables = ref([{ name: 'shit' }]);
    const indicies = ref([]);
    const views = ref([]);
    const triggers = ref([]);
    const editor = shallowRef();
    const selectedCode = shallowRef('');
    const results = ref([]);

    const MONACO_EDITOR_OPTIONS = {
        automaticLayout: true,
        formatOnType: true,
        formatOnPaste: true,
    }

    const database = gateway.getRelationalDataStorage(uniqueId, isSaveSpecific);
    let schemaScanQueryId;
    database.queryCompleted.addListener(result => {
        results.value = [
            {
                errorCode: result.errorCode,
                errorMessage: result.errorMessage,
                executionSeconds: result.executionSeconds,
                executionDuration: dayjs.duration(result.executionSeconds, 'seconds'),
                extendedErrorCode: result.extendedErrorCode,
                queryId: result.queryId,
                recordSets: result.recordSets.map(recordSet => {
                    return {
                        fieldNames: recordSet.fieldNames,
                        items: recordSet.records.map(record => {
                            const item = {};
                            recordSet.fieldNames.forEach((fieldName, fieldIndex) => item[fieldName] = record[fieldIndex]);
                            return item;
                        }),
                        records: recordSet.records,
                    };
                }),
                tag: result.tag,
            },
            ...results.value,
        ];
        if (result.queryId === schemaScanQueryId) {
            const newTables = [];
            const tableByName = {};
            result.recordSets[0].records.forEach(record => {
                const newTable = {
                    columns: [],
                    name: record[0],
                    sql: record[1],
                };
                newTables.push(newTable);
                tableByName[newTable.name] = newTable;
            });
            result.recordSets[1].records.forEach(record => {
                tableByName[record[0]].columns.push({
                    defaultValue: record[4],
                    isNotNull: !!record[3],
                    isPrimaryKey: !!record[5],
                    name: record[1],
                    type: record[2],
                });
            });
            tables.value = newTables;
            indicies.value = result.recordSets[2].records.map(record => {
                return {
                    name: record[0],
                    sql: record[2],
                    table: record[1],
                };
            });
            const newViews = [];
            const viewByName = {};
            result.recordSets[3].records.forEach(record => {
                const newView = {
                    columns: [],
                    name: record[0],
                    sql: record[1],
                };
                newViews.push(newView);
                viewByName[newView.name] = newView;
            });
            result.recordSets[4].records.forEach(record => {
                viewByName[record[0]].columns.push({
                    name: record[1],
                    type: record[2],
                });
            });
            views.value = newViews;
            triggers.value = result.recordSets[5].records.map(record => {
                return {
                    name: record[0],
                    sql: record[2],
                    table: record[1],
                };
            });
        }
    });
    
    function handleSendAllAndRun() {
        database.execute(tabState.code);
    }

    function handleSendSelectionAndRun() {
        database.execute(selectedCode.value);
    }

    function replaceSelectedCode(replacement) {
        const ed = editor.value;
        ed.executeEdits('replace', [
            {
                range: ed.getSelection(),
                text: replacement,
                forceMoveMarkers: true,
            }
        ]);
    }

    function generateTableSelect(table) {
        replaceSelectedCode(`SELECT${table.columns.map(column => `
    "${column.name}"`).join(',')}
FROM
    "main"."${table.name}"`);
    }

    function generateTableInsert(table) {
        replaceSelectedCode(`INSERT INTO "main"."${table.name}" (
    ${table.columns.map(column => `"${column.name}"${column.isPrimaryKey ? ' /* if this primary key is autonumbered, remove it and let SQLite provide a value */' : ''}`).join(`,
    `)}
) VALUES (
    ${table.columns.map(column => column.type === 'TEXT' ? `''` : column.type === 'BINARY' ? `X'' -- place hex between single quotes` : column.type === 'INTEGER' ? `0${column.isPrimaryKey ? ' /* if this primary key is autonumbered, remove it and let SQLite provide a value */' : ''}` : `0.0`).join(`,
    `)}
)`);
    }

    function generateTableDrop(table) {
        replaceSelectedCode(`DROP TABLE "main"."${table.name}"`);
    }

    function generateIndexDropAndCreate(index) {
        replaceSelectedCode(`DROP INDEX IF EXISTS "main"."${index.name}";
${index.sql}`);
    }

    function generateViewDrop(view) {
        replaceSelectedCode(`DROP VIEW "main"."${view.name}"`);
    }

    function generateTriggerDropAndCreate(trigger) {
        replaceSelectedCode(`DROP TRIGGER "main"."${trigger.name}";
${trigger.sql}`);
    }

    function openSqliteErrorDocumentation() {
        gateway.openUrl('https://www.sqlite.org/rescode.html');
    }

    function handleMount(editorInstance) {
        editor.value = editorInstance;
        editorInstance.onDidChangeCursorSelection(() => {
            const selection = editorInstance.getSelection();
            if (selection) {
                const selectedTextValue = editorInstance.getModel().getValueInRange(selection);
                selectedCode.value = selectedTextValue;
            } else {
                selectedCode.value = '';
            }
        });
    }

    function getJavaScriptText(query) {
        return `const uniqueId = '${uniqueId}';
const database = gateway.getRelationalDataStorage(uniqueId, ${isSaveSpecific ? 'true' : 'false'});

let queryId;

database.queryCompleted.addListener(result => {
    // could also be looking at result.tag here
    if (result.queryId === queryId) {
        // result.errorCode, result.extendedErrorCode being non-zero is sus
        // result.errorMessage being something other than null or empty string is sus
        // result.executionSeconds is the number of seconds SQLite was working if you're curious
        result.recordSets.forEach(recordSet => {
            // recordSet.fieldNames is an array of strings
            recordSet.records.forEach(record => {
                record.forEach(value => {
                    // this could be a string, a number, or even a Uint8Array if it's a SQLite BINARY value
                });
            });
        });
    }
});

// the third argument is the query parameters which you can use to protect from SQL injection!
queryId = database.execute(\`${query}\`, 'this is the tag', {})`;
    }

    function getPythonText(query) {
        return `try:
    from plumbbuddy_proxy.asynchronous import listen_for
    from plumbbuddy_proxy.api import gateway
    from uuid import UUID
    unique_id = UUID('${uniqueId}')
    database = gateway.get_relational_data_storage(unique_id, ${isSaveSpecific ? 'True' : 'False'})

    query_id = None

    @listen_for(database.query_completed)
    def handle_query_completed(result):
        # could also be looking at result.tag here
        if result.query_id == query_id:
            # result.error_code, result.extended_error_code being non-zero is sus
            # result.error_message being something other than None or empty string is sus
            # result.execution_time is a timedelta if you're curious about how long SQLite was working
            for record_set in result.record_sets:
                for field_name in record_set.field_names:
                    pass
                for record in record_set.records:
                    for value in record:
                        # this could be a str, a float, or even bytes if it's a SQLite BINARY value
                        pass
    
    # the third argument is a dict of query parameters which you can use to protect from SQL injection!
    query_id = database.execute('''${query}''', 'this is the tag', {})

except ModuleNotFoundError:
    # either PlumbBuddy is unavailable or RMI has been disabled by the player
    # handling this is the mod's responsibility, unfortunately
    pass`;
    }

    const examplePythonAllCode = computed(() => getPythonText(tabState.code));
    const examplePythonSelectedCode = computed(() => getPythonText(selectedCode.value));
    const exampleJavaScriptAllCode = computed(() => getJavaScriptText(tabState.code));
    const exampleJavaScriptSelectedCode = computed(() => getJavaScriptText(selectedCode.value));

    function refreshSchema() {
        schemaScanQueryId = database.execute(`
            SELECT
                name,
                sql
            FROM
                sqlite_master
            WHERE
                type = 'table'
                AND name NOT LIKE 'sqlite_%'
            ORDER BY
                name;

            SELECT 
                m.name [table],
                p.name [column],
                p.type,
                p.[notnull],
                p.dflt_value,
                p.pk
            FROM 
                sqlite_master m
            JOIN 
                pragma_table_info(m.name) p
            WHERE 
                m.type = 'table'
                AND m.name NOT LIKE 'sqlite_%'
            ORDER BY 
                m.name,
                p.cid;

            SELECT 
                name [index],
                tbl_name [table],
                sql
            FROM 
                sqlite_master
            WHERE 
                type = 'index'
                AND name NOT LIKE 'sqlite_%'
            ORDER BY 
                tbl_name,
                name;

            SELECT 
                name,
                sql
            FROM 
                sqlite_master
            WHERE 
                type = 'view'
            ORDER BY 
                name;

            SELECT 
                m.name [view],
                c.name [column],
                c.type
            FROM 
                sqlite_master m
            JOIN 
                pragma_table_info(m.name) c
            WHERE 
                m.type = 'view'
            ORDER BY 
                m.name,
                c.cid;

            SELECT 
                name [trigger],
                tbl_name [table],
                sql
            FROM 
                sqlite_master
            WHERE 
                type = 'trigger'
            ORDER BY 
                tbl_name,
                name;
            `, 'ts4_rds_browser_schema_scan')
    }

    onMounted(() => {
        refreshSchema();
    });
</script>
