# Menggunakan image dasar untuk Android
FROM ubuntu:latest

# Install dependensi untuk emulator Android dan Appium
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    android-sdk \
    android-emulator \
    appium \
    git \
    curl \
    wget \
    unzip \
    python3 \
    python3-pip \
    npm

# Install Appium
RUN npm install -g appium

# Set environment variables untuk SDK dan emulator
ENV ANDROID_HOME=/usr/local/android-sdk
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# Install Appium dependencies
RUN pip3 install appium-python-client

# Set up Android SDK
RUN curl -o android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip \
    && unzip android-sdk.zip -d /usr/local \
    && rm android-sdk.zip

# Download emulator system image
RUN /usr/local/android-sdk/tools/bin/sdkmanager --install "system-images;android-29;google_apis;x86"

# Set up Android Virtual Device (AVD)
RUN echo no | /usr/local/android-sdk/tools/bin/avdmanager create avd --name "test_avd" --package "system-images;android-29;google_apis;x86"

# Expose Appium port
EXPOSE 4723

# Jalankan Appium dan emulator
CMD ["appium"]
