<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision/v1/image_annotator.proto

namespace Google\Cloud\Vision\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * A list of requests to annotate files using the BatchAnnotateFiles API.
 *
 * Generated from protobuf message <code>google.cloud.vision.v1.BatchAnnotateFilesRequest</code>
 */
class BatchAnnotateFilesRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * Required. The list of file annotation requests. Right now we support only one
     * AnnotateFileRequest in BatchAnnotateFilesRequest.
     *
     * Generated from protobuf field <code>repeated .google.cloud.vision.v1.AnnotateFileRequest requests = 1 [(.google.api.field_behavior) = REQUIRED];</code>
     */
    private $requests;
    /**
     * Optional. Target project and location to make a call.
     * Format: `projects/{project-id}/locations/{location-id}`.
     * If no parent is specified, a region will be chosen automatically.
     * Supported location-ids:
     *     `us`: USA country only,
     *     `asia`: East asia areas, like Japan, Taiwan,
     *     `eu`: The European Union.
     * Example: `projects/project-A/locations/eu`.
     *
     * Generated from protobuf field <code>string parent = 3;</code>
     */
    private $parent = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type \Google\Cloud\Vision\V1\AnnotateFileRequest[]|\Google\Protobuf\Internal\RepeatedField $requests
     *           Required. The list of file annotation requests. Right now we support only one
     *           AnnotateFileRequest in BatchAnnotateFilesRequest.
     *     @type string $parent
     *           Optional. Target project and location to make a call.
     *           Format: `projects/{project-id}/locations/{location-id}`.
     *           If no parent is specified, a region will be chosen automatically.
     *           Supported location-ids:
     *               `us`: USA country only,
     *               `asia`: East asia areas, like Japan, Taiwan,
     *               `eu`: The European Union.
     *           Example: `projects/project-A/locations/eu`.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Google\Cloud\Vision\V1\ImageAnnotator::initOnce();
        parent::__construct($data);
    }

    /**
     * Required. The list of file annotation requests. Right now we support only one
     * AnnotateFileRequest in BatchAnnotateFilesRequest.
     *
     * Generated from protobuf field <code>repeated .google.cloud.vision.v1.AnnotateFileRequest requests = 1 [(.google.api.field_behavior) = REQUIRED];</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getRequests()
    {
        return $this->requests;
    }

    /**
     * Required. The list of file annotation requests. Right now we support only one
     * AnnotateFileRequest in BatchAnnotateFilesRequest.
     *
     * Generated from protobuf field <code>repeated .google.cloud.vision.v1.AnnotateFileRequest requests = 1 [(.google.api.field_behavior) = REQUIRED];</code>
     * @param \Google\Cloud\Vision\V1\AnnotateFileRequest[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setRequests($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Google\Cloud\Vision\V1\AnnotateFileRequest::class);
        $this->requests = $arr;

        return $this;
    }

    /**
     * Optional. Target project and location to make a call.
     * Format: `projects/{project-id}/locations/{location-id}`.
     * If no parent is specified, a region will be chosen automatically.
     * Supported location-ids:
     *     `us`: USA country only,
     *     `asia`: East asia areas, like Japan, Taiwan,
     *     `eu`: The European Union.
     * Example: `projects/project-A/locations/eu`.
     *
     * Generated from protobuf field <code>string parent = 3;</code>
     * @return string
     */
    public function getParent()
    {
        return $this->parent;
    }

    /**
     * Optional. Target project and location to make a call.
     * Format: `projects/{project-id}/locations/{location-id}`.
     * If no parent is specified, a region will be chosen automatically.
     * Supported location-ids:
     *     `us`: USA country only,
     *     `asia`: East asia areas, like Japan, Taiwan,
     *     `eu`: The European Union.
     * Example: `projects/project-A/locations/eu`.
     *
     * Generated from protobuf field <code>string parent = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setParent($var)
    {
        GPBUtil::checkString($var, True);
        $this->parent = $var;

        return $this;
    }

}
