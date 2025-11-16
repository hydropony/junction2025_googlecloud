package org.example.config

import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Value
import org.springframework.boot.web.servlet.FilterRegistrationBean
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.core.Ordered
import org.springframework.web.cors.CorsConfiguration
import org.springframework.web.cors.UrlBasedCorsConfigurationSource
import org.springframework.web.filter.CorsFilter

@Configuration
class CorsConfig(
    @Value(
        "\${app.cors.allowed-origins:http://localhost:1234,http://127.0.0.1:1234,https://aimo-fresh-connect.lovable.app,https://aimo-fresh-connect.lovable.app/checkout}"
    )
    private val allowedOrigins: String
) {
    private val logger = LoggerFactory.getLogger(CorsConfig::class.java)
    private val normalizedOrigins: List<String> = parseAllowedOrigins()

    @Bean
    fun corsConfigurationSource(): UrlBasedCorsConfigurationSource {
        val config = CorsConfiguration().apply {
            allowedOrigins = normalizedOrigins
            allowedOriginPatterns = normalizedOrigins
            allowedMethods = listOf("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
            allowedHeaders = listOf("*")
            allowCredentials = false
            maxAge = 3600
        }

        logger.info("Configured CORS origins: {}", normalizedOrigins)

        return UrlBasedCorsConfigurationSource().apply {
            registerCorsConfiguration("/**", config)
        }
    }

    @Bean
    fun corsFilter(source: UrlBasedCorsConfigurationSource): CorsFilter =
        CorsFilter(source)

    @Bean
    fun corsFilterRegistration(filter: CorsFilter): FilterRegistrationBean<CorsFilter> =
        FilterRegistrationBean(filter).apply {
            order = Ordered.HIGHEST_PRECEDENCE
        }

    private fun parseAllowedOrigins(): List<String> =
        allowedOrigins
            .split(",")
            .map { it.trim().removeSuffix("/") }
            .filter { it.isNotEmpty() }
            .distinct()
}

