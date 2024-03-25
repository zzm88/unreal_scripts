// Fill out your copyright notice in the Description page of Project Settings.


#include "MyBlueprintFunctionLibrary.h"
#include "Camera/CameraActor.h"
#include "EngineUtils.h"

ACameraActor* UMyBlueprintFunctionLibrary::FindCameraByTag(UWorld* World, FString CameraName)
{
    for (TActorIterator<ACameraActor> It(World); It; ++It)
    {
//print out the name of the camera actor
        UE_LOG(LogTemp, Warning, TEXT("Camera Name: %s"), *It->GetName());
        //convert CameraName to FName
        FName CameraFName = FName(*CameraName);
            
        if (It->Tags.Contains(CameraFName))
        {
            return *It;
        }
    }

    return nullptr;
}
