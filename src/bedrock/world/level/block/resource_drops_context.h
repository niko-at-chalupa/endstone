// Copyright (c) 2024, The Endstone Project. (https://endstone.dev) All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

enum class ResourceDropsCause : int {
    PlayerMining = 0,
    Explosion = 1,
    ProjectileHit = 2,
    Other = 3,
};

struct ResourceDropsContext {
    static ResourceDropsContext fromPlayerMining(const IBlockSource &block_source, const BlockPos &position,
                                                 const ItemStack &used_item);
    static ResourceDropsContext fromExplosion(const IBlockSource &block_source, float explosion_radius,
                                              const BlockPos &position);
    static ResourceDropsContext fromProjectileHit(const IBlockSource &block_source, const BlockPos &position);
    static ResourceDropsContext fromOtherCause(const IBlockSource &block_source, const BlockPos &position)
    {
        return {ResourceDropsCause::Other,    1.0, ItemStack::EMPTY_ITEM, block_source, position,
                block_source.getDimensionId()};
    }
    static ResourceDropsContext fromLootResolver(const IBlockSource &block_source, const BlockPos &position,
                                                 const ItemStack &used_item);
    [[nodiscard]] Random &getRandom() const;
    [[nodiscard]] ILevel &getLevel() const;
    [[nodiscard]] bool isUsingSilkTouch() const;
    [[nodiscard]] int getMiningLootBonusLevel() const;
    [[nodiscard]] const BlockActor *getBlockActor() const;
    ResourceDropsCause cause;
    float explosion_radius;
    const ItemStack &used_item;
    const BlockPos block_pos;
    const DimensionType dimension_type;

private:
    ResourceDropsContext(ResourceDropsCause cause, float explosion_radius, const ItemStack &used_item,
                         const IBlockSource &block_source, const BlockPos &block_pos, DimensionType dimension_type)
        : cause(cause), explosion_radius(explosion_radius), used_item(used_item), block_pos(block_pos),
          dimension_type(dimension_type), block_source_(block_source)
    {
    }
    const IBlockSource &block_source_;
};
