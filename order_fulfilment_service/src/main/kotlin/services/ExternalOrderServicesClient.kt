package org.example.services

import org.example.config.ExternalServicesProperties
import org.example.dto.PredictOrderResponse
import org.example.dto.ProductDto
import org.example.dto.ShortageProactiveRequest
import org.example.dto.ShortageProactiveResponse
import org.example.dto.SubstitutionRequest
import org.example.dto.SubstitutionResponse
import org.springframework.stereotype.Component
import org.springframework.web.client.RestTemplate

@Component
class ExternalOrderServicesClient(
    private val restTemplate: RestTemplate,
    private val externalServicesProperties: ExternalServicesProperties
) {
    fun getItemsToReplace(order: ProductDto): PredictOrderResponse {
        return restTemplate.postForObject(
            externalServicesProperties.predictOrderUrl,
            order,
            PredictOrderResponse::class.java
        ) ?: PredictOrderResponse(emptyList())
    }

    fun getSubstitutionsForItem(
        lineId: Int,
        productCode: String,
        qty: Double
    ): SubstitutionResponse {
        val request = SubstitutionRequest(lineId, productCode, qty)

        return restTemplate.postForObject(
            externalServicesProperties.substitutionSuggestUrl,
            request,
            SubstitutionResponse::class.java
        ) ?: SubstitutionResponse(lineId, emptyList())
    }

    fun getShortageDecisions(request: ShortageProactiveRequest): ShortageProactiveResponse {
        return restTemplate.postForObject(
            externalServicesProperties.shortageUrl,
            request,
            ShortageProactiveResponse::class.java
        ) ?: ShortageProactiveResponse(emptyList())
    }
}
