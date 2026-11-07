/* Lightweight independent catalogue sanity check; no third-party JSON library. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static char *read_file(const char *path, long *length) {
    FILE *fp = fopen(path, "rb");
    if (!fp) return NULL;
    if (fseek(fp, 0, SEEK_END) != 0) { fclose(fp); return NULL; }
    long size = ftell(fp);
    if (size < 0 || fseek(fp, 0, SEEK_SET) != 0) { fclose(fp); return NULL; }
    char *buffer = (char *)malloc((size_t)size + 1);
    if (!buffer) { fclose(fp); return NULL; }
    size_t got = fread(buffer, 1, (size_t)size, fp);
    fclose(fp);
    if (got != (size_t)size) { free(buffer); return NULL; }
    buffer[size] = '\0';
    *length = size;
    return buffer;
}

static size_t count_key(const char *json, const char *key) {
    size_t count = 0;
    const char *p = json;
    while ((p = strstr(p, key)) != NULL) { count++; p += strlen(key); }
    return count;
}

static int read_string_value(const char *p, char *out, size_t cap) {
    while (*p && isspace((unsigned char)*p)) p++;
    if (*p++ != '"') return 0;
    size_t n = 0;
    while (*p && *p != '"') {
        if (*p == '\\' && p[1]) p++;
        if (n + 1 >= cap) return 0;
        out[n++] = *p++;
    }
    if (*p != '"') return 0;
    out[n] = '\0';
    return 1;
}

static int check_nonempty_formula_values(const char *json) {
    const char *p = json;
    const char *key = "\"formula\":";
    while ((p = strstr(p, key)) != NULL) {
        char value[4096];
        p += strlen(key);
        if (!read_string_value(p, value, sizeof(value)) || value[0] == '\0') return 0;
    }
    return 1;
}

static int check_unique_ids(const char *json, size_t expected) {
    char **ids = (char **)calloc(expected, sizeof(char *));
    if (!ids) return 0;
    size_t count = 0;
    const char *p = json;
    const char *key = "\"id\":";
    int ok = 1;
    while ((p = strstr(p, key)) != NULL) {
        char value[256];
        p += strlen(key);
        if (count >= expected || !read_string_value(p, value, sizeof(value)) || value[0] == '\0') { ok = 0; break; }
        for (size_t i = 0; i < count; i++) {
            if (strcmp(ids[i], value) == 0) { ok = 0; break; }
        }
        if (!ok) break;
        ids[count] = (char *)malloc(strlen(value) + 1);
        if (!ids[count]) { ok = 0; break; }
        strcpy(ids[count], value);
        count++;
    }
    if (count != expected) ok = 0;
    for (size_t i = 0; i < count; i++) free(ids[i]);
    free(ids);
    return ok;
}

int main(int argc, char **argv) {
    const char *path = argc > 1 ? argv[1] : "data.json";
    long length = 0;
    char *json = read_file(path, &length);
    if (!json) { fprintf(stderr, "FAIL: cannot read %s\n", path); return 1; }

    const size_t subjects = count_key(json, "\"id\":");
    const size_t units = count_key(json, "\"formulas\": [");
    const size_t formulas = count_key(json, "\"formula\":");
    int ok = subjects > 0 && units == subjects * 5 && formulas > 0;
    ok = ok && check_unique_ids(json, subjects) && check_nonempty_formula_values(json);

    if (ok) {
        printf("PASS: %zu subjects, %zu units, %zu formulas (%ld bytes)\n", subjects, units, formulas, length);
    } else {
        fprintf(stderr, "FAIL: catalogue count/ID/formula check failed (subjects=%zu units=%zu formulas=%zu)\n", subjects, units, formulas);
    }
    free(json);
    return ok ? 0 : 1;
}
