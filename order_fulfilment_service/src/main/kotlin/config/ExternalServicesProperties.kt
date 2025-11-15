package org.example.config

import org.springframework.boot.context.properties.ConfigurationProperties

@ConfigurationProperties(prefix = "external-services")
data class ExternalServicesProperties(
    val predictOrderUrl: String,
    val substitutionSuggestUrl: String,
    val shortageUrl: String
)

