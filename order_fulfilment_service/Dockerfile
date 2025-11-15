FROM eclipse-temurin:21-jre-alpine AS runtime

WORKDIR /app

# Copy the built Spring Boot fat jar into the image
COPY build/libs/order_fulfilment_service-*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app/app.jar"]


