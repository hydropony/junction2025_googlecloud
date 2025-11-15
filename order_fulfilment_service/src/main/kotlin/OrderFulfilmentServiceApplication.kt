package org.example

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

import org.example.config.ExternalServicesProperties
import org.springframework.boot.context.properties.EnableConfigurationProperties

@SpringBootApplication
@EnableConfigurationProperties(ExternalServicesProperties::class)
class OrderFulfilmentServiceApplication

fun main(args: Array<String>) {
    runApplication<OrderFulfilmentServiceApplication>(*args)
}