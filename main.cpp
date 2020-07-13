#include <tobii/tobii.h>
#include <tobii/tobii_streams.h>
#include <stdio.h>
#include <assert.h>
#include <cstring>

#include <chrono>

#include <fstream>

auto begin = std::chrono::high_resolution_clock::now();

int count = 0; //how many readings have been made so far

std::ofstream outputFile;

void gaze_point_callback(tobii_gaze_point_t const *gaze_point, void *user_data) {
    
    auto end = std::chrono::high_resolution_clock::now();
    auto dur = end - begin;
    auto ms = std::chrono::duration_cast<std::chrono::microseconds>(dur).count();

    

    if (gaze_point->validity == TOBII_VALIDITY_VALID) {
        printf("Reading %d, At time %ld, Gaze point: %f, %f\n", count, ms,
               gaze_point->position_xy[0],
               gaze_point->position_xy[1]);
        outputFile << count << ',' << ms << ',' << gaze_point->position_xy[0]
            << ',' << gaze_point->position_xy[1] << std::endl;
        count++;
    }
        
}

static void url_receiver(char const *url, void *user_data) {
    char *buffer = (char *) user_data;
    if (*buffer != '\0') return; // only keep first value

    if (strlen(url) < 256)
        strcpy(buffer, url);
}

int main() {

    outputFile.open("GazeReading.csv");
    outputFile << "Reading, Time (micro), X Coord, Y Coord\n";

    tobii_api_t *api;
    tobii_error_t error = tobii_api_create(&api, NULL, NULL);
    assert(error == TOBII_ERROR_NO_ERROR);

    char url[256] = {0};
    error = tobii_enumerate_local_device_urls(api, url_receiver, url);
    assert(error == TOBII_ERROR_NO_ERROR && *url != '\0');

    tobii_device_t *device;
    error = tobii_device_create(api, url, &device);
    assert(error == TOBII_ERROR_NO_ERROR);

    error = tobii_gaze_point_subscribe(device, gaze_point_callback, 0);
    assert(error == TOBII_ERROR_NO_ERROR);

    int is_running = 1000; // in this sample, exit after some iterations, 1000 is 10 seconds roughly
    while (--is_running > 0) {
        error = tobii_wait_for_callbacks(1, &device);
        assert(error == TOBII_ERROR_NO_ERROR || error == TOBII_ERROR_TIMED_OUT);

        error = tobii_device_process_callbacks(device);
        assert(error == TOBII_ERROR_NO_ERROR);
    }

    outputFile.close();

    error = tobii_gaze_point_unsubscribe(device);
    assert(error == TOBII_ERROR_NO_ERROR);

    error = tobii_device_destroy(device);
    assert(error == TOBII_ERROR_NO_ERROR);

    error = tobii_api_destroy(api);
    assert(error == TOBII_ERROR_NO_ERROR);
    return 0;
}