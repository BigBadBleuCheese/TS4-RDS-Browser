/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify';
import pinia from '@/stores';

import hljs from 'highlight.js/lib/core';
import javascript from 'highlight.js/lib/languages/javascript';
import python from 'highlight.js/lib/languages/python';
import sql from 'highlight.js/lib/languages/sql';
import hljsVuePlugin from "@highlightjs/vue-plugin";

hljs.registerLanguage('javascript', javascript);
hljs.registerLanguage('python', python);
hljs.registerLanguage('sql', sql);

export function registerPlugins (app) {
    app
        .use(vuetify)
        .use(pinia)
        .use(hljsVuePlugin)
}
