package org.example.controller

import org.example.dto.CreateClaimRequest
import org.example.dto.PickShortageEventRequest
import org.example.dto.StubDescriptionResponse
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/orders")
class OrderEventsController {

    /**
     * SEPARATE flow: triggered when a picker detects a shortage during picking.
     * Implementation should:
     *  1. Flag the related order line as short_pick to persist the shortage fact.
     *  2. Call Substitution Service to request replacement options.
     *  3. Notify Communication Orchestrator so the customer can be contacted in real time.
     */
    @PostMapping("/events/pick-shortage")
    fun registerPickShortageEvent(
        @RequestBody payload: PickShortageEventRequest
    ): ResponseEntity<StubDescriptionResponse> {
        val description = listOf(
            "Mark order line #${payload.lineId} as short_pick so the shortage is recorded.",
            "Query Substitution Service for replacements for product ${payload.productCode}.",
            "Trigger Communication Orchestrator to contact the customer during picking."
        )

        return ResponseEntity
            .status(HttpStatus.NOT_IMPLEMENTED)
            .body(
                StubDescriptionResponse(
                    endpoint = "/api/orders/events/pick-shortage",
                    description = description
                )
            )
    }

    /**
     * Claim creation after delivery (invoked by Communication Orchestrator or NLU).
     * Implementation should:
     *  1. Call Multimodal Evidence Service when attachments (photos, etc.) must be validated.
     *  2. Decide on the claim outcome and trigger Compensation or other flows if required.
     */
    @PostMapping("/claims/create")
    fun createClaim(
        @RequestBody payload: CreateClaimRequest
    ): ResponseEntity<StubDescriptionResponse> {
        val description = listOf(
            "Persist the complaint context for order ${payload.orderId} submitted via ${payload.channel}.",
            "Request Multimodal Evidence Service to validate provided attachmentIds.",
            "Based on the evaluation, call Compensation and orchestrate follow-up back-office actions."
        )

        return ResponseEntity
            .status(HttpStatus.NOT_IMPLEMENTED)
            .body(
                StubDescriptionResponse(
                    endpoint = "/api/orders/claims/create",
                    description = description
                )
            )
    }
}
